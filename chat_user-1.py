import os
import openai
from dotenv import load_dotenv

load_dotenv()

def chat_with_gpt(prompt):
    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # ou modelo que atue confrome as intençoes do usuário
        messages=[
            {"role": "system", "content": "atualizar pagamento", "acompanhar pedido", "rastrear o produto", "status de entrega", },
            {"role": "user", "content": prompt}, 
        ]         
    )

    function 
    input() # após ser o comando será necessário voltar ao dicionário de intenções para encontrar a intenção utilizando expressões regulares. 
    

    return response.choices[0].message['content']

print(chat_with_gpt("Onde vejo o status do meu pedido?", "Como faço para rastrear meu pedido?", "Quero saber onde está meu pedido, como faço?", "Status de entrega, como consultar?")