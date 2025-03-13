from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os 
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class EmailRequest(BaseModel):
    name: str
    email: EmailStr
    message: str


@app.post("/send-email")
def send_email(request: EmailRequest):
    conteudo = f"Tem uma mensagem nova! \n Nome: {request.name} \n Email: {request.email} \n Mensagem: {request.message}"

    try:
        sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
        
        from_email = Email(os.getenv("FROM_EMAIL"))  
        to_email = To(os.getenv("TO_EMAIL"))  
        subject = f"Messagem nova de {request.name}"
        content = Content("text/plain", conteudo)  

        mail = Mail(from_email, to_email, subject, content)

        response = sg.send(mail)

        return {"status": "success", "message": "Correo enviado exitosamente", "status_code": response.status_code}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Deu erro: {str(e)}")