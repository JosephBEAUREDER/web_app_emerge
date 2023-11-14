from bardapi import Bard
from bardapi import Bard, max_token, max_sentence
import os
import time

os.environ['_BARD_API_KEY'] = 'bQjTqbzcKVklVwwhxLJxYKSnOauhKWFzMzZTMOL0P279BK3ygFLr2fg_716QP1SuYt8CuA.'

text_text = "Write only two short sentences about this : Le malentendu de Jérusalem a eu lieu en l'an 50"

text = "Tell me someting"

# print((Bard().get_answer(text_text)['content'], 1))

# print(max_sentence(Bard().get_answer("Les sociétés et l'Etat")['content'], 1))
