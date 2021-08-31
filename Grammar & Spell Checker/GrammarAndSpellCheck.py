from gingerit.gingerit import GingerIt
from googletrans import Translator
import streamlit as st


trans = Translator()

st.title('Grammar & Spell Checker')
text = st.text_area("Enter Text:")
parser = GingerIt()

if st.button('Correct Sentence'):
   
    if text == '':
        st.write('Please enter text for checking') 
    else: 
        result_dict = parser.parse(text)
        text = result_dict
        st.markdown('**Corrected Sentence - **' + str(result_dict["result"]))
        # x=text.replace(text,str(result_dict["result"]))
        x = str(result_dict["result"])
        t = trans.translate(x, src='en' , dest='hi')
        st.markdown('**In Hindi - **' + str({t.text}))
        print(x)
        
else: pass

# if st.button('Convert In Hindi'):
#      print(x)
#      t = trans.translate(x, src='en' , dest='hi')
#      st.markdown('**In Hindi - **' + str({t.text}))
#      print(f'{t.origin} -> {t.text}')
    
# else:pass

