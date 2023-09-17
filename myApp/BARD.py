from bardapi import Bard
import os
import time

os.environ['_BARD_API_KEY'] = 'bAibCmliNrjMy1lcLUtlt41skcvHcb2SiupbWoIvVG81fqEWmbZ_lmqrLlynYU67jmWUiA.'

text_text = "Qui est le président des fesses ?"

print((Bard().get_answer(text_text)['content']))