import os
from openai import OpenAI

def create_img(set_prompt):
    # 環境変数にAPIキーを設定しておく
    set_key = os.environ.get('OPENAI_API_KEY_for_DALLE3')
    if set_key is None:
        raise ValueError("APIキーが設定されていません。")
    client = OpenAI(api_key=set_key)

    response = client.images.generate(
        model="dall-e-3",
        prompt=set_prompt,
        size="1024x1024",# ['256x256', '512x512', '1024x1024', '1024x1792', '1792x1024']
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)

# プロンプトを入力
# set_prompt="An old man driving a motorcycle while drinking beer.big smile"
# set_prompt="school girl,japanese anime style"
# set_prompt="初音ミクのようなキャラクター,金髪,アニメ絵"
set_prompt="主人公,全身,笑顔,アニメ絵"
create_img(set_prompt)