import streamlit as st
from keras.models import load_model
st.title("hello")
import os

model=load_model("C:/Users/abhia/Downloads/modelvgg_weights.h5")
labels=[0,1,2,3]

btn = st.button("predict")

if btn:
    crop = filename.astype('float32') / 255
    labs = np.array(labs)

    pred= model.predict(labs) 
    print(pred)
    st.subheader(pred)

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)


if __name__ == '__main__':
    # Select a file
    if st.checkbox('Select a file in current directory'):
        folder_path = '.'
        if st.checkbox('Change directory'):
            folder_path = st.text_input('Enter folder path', '.')
        filename = file_selector(folder_path=folder_path)
        st.write('You selected `%s`' % filename)





