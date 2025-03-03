from transformers import pipeline
import gradio as gr


model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    print('hello')
    return summary


# create an interface for the model
with gr.Interface(predict, "textbox", "text") as interface:
    interface.launch()


# with gr.Blocks() as demo:
#     textbox = gr.Textbox(placeholder = "Enter text to summarize", lines=4)
#     gr.Interface(fn= predict, inputs = textbox, outputs = 'text')

# demo.launch()
