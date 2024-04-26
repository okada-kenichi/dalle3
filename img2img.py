
import os
from openai import OpenAI

def create_img():
    # 環境変数にAPIキーを設定しておく
    set_key = os.environ.get('OPENAI_API_KEY_for_DALLE3')
    if set_key is None:
        raise ValueError("APIキーが設定されていません。")
    client = OpenAI(api_key=set_key)

    response = client.images.edit(
        model="dall-e-2",
        # image=open("img/miku.png", "rb"),
        # mask=open("img/miku_mask.png", "rb"),
        image=open("jk/jk.png", "rb"),
        mask=open("jk/jk_mask.png", "rb"),
        prompt="困った表情,アニメ絵",
        n=1,
        size="1024x1024"
        )
    image_url = response.data[0].url
    print(image_url)
create_img()