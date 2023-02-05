import gradio as gr
import cv2

def image_classifier(inp):
    return {'cat': 0.3, 'dog': 0.7}

def to_black(image):
    output = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return output



def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

def dreambooth(pic_input_path, txt_input_path,):
    return pic_input_path, txt_input_path

demo = gr.Interface(
    fn=dreambooth,
    inputs=["text", "text",],
    outputs=["text",],
)


# demo = gr.Interface(fn=to_black, inputs="image", outputs="image")
demo.launch()