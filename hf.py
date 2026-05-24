import config
from huggingface_hub import InferenceClient
MODELS=getattr(config, "HF_MODELS", ["meta-llama/Llama-3.1-8B-Instruct"])
def generate_response(prompt:str,temperature:float=0.3,max_tokens: int=530)->str:
    apikey=getattr(config,'HFAPIKEY',None)
    if not apikey:
        return 'Error:HUGGING FACE API KEY NOT FOUND'
    #send the requests to the groq model
    client=InferenceClient(MODELS,token=apikey)
    #create a chart structure
    response=client.chat.completions.create(
        model=MODELS[1],
        messages=[{'role':'user','content':prompt}],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content