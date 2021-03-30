from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('final_tuned_first_model_titanic_28Mar2021')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def main():

    from PIL import Image
    image = Image.open('labs.jpg')
    img_if = Image.open('ifserra.jpg')

    st.image(image,use_column_width=False)

    add_selectbox = st.sidebar.selectbox(
    "Forma de predição?",
    ("Online", "Batch"))

    st.title("App de Predição - Survived")
    st.sidebar.info('Verificar se com base nas informações o tripulante do Titanic sobreviveu ou não!')
    st.sidebar.success('https://www.github.com/disciplabs')  
    st.sidebar.image(img_if)

    if add_selectbox == 'Online':

        Age = st.number_input('Idade', min_value=1, max_value=100, value=22)
        Sex = st.selectbox('Sexo', ['male', 'female'])
        Fare = st.number_input('Fare', min_value=1, max_value=512, value=7)
        Pclass = st.selectbox('Classe', [1,2,3])
        Parch = st.selectbox('Filhos', [0,1,2,3,4,5,6,7,8])
        output=""
        
        input_dict = {'Pclass' : Pclass,'Sex' : Sex, 'Age' : Age, 'Fare' : Fare,'Parch' : Parch}

        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output =  str(output)
            if output=='1':
                res = """
                        [Sobreviveu] 
                        (obs: dados também podem estar referenciados como 1/sim) 
                        """
            else:
                res = """
                        [Não Sobreviveu] 
                        (obs: dados também podem estar referenciados como 0/não) 
                        """
            st.success('O resultado é: {}'.format(res))


    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload arquivo csv para predições", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    main()
