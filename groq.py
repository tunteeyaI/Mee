import config
from openai import OpenAI
GROQURL="https://api.groq.com/openai/v1"
MODELS=getattr(config, "GROQ_MODELS",["llama-3.1-8b-instant","mixtral-8x7b-32768"])
def generate_response(prompt:str,temperature:float=0.3,max_tokens: int=530)->str:
    apikey=getattr(config,'GROQAPIKEY',None)
    if not apikey:
        return 'Error:GROQ API KEY NOT FOUND'
    #send the requests to the groq model
    client=OpenAI(api_key=apikey,base_url=GROQURL)
    #create a chart structure
    response=client.chat.completions.create(
        model=MODELS[0],
        messages=[{'role':'user','content':prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.contentv