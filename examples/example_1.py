from context import prosomoiahelper

texts = []

texts.append("""Pelagia most ven’rable, * with all temp’rance and toil didst thou * mortify thy body while
quickening thy soul, * making it fair; and becoming an abode of the Comforter, * thou wast
mysticly made one * with thy Bridegroom and Fashioner. * Him do thou entreat * to deliver
from perils and corruption them that faithfully do honor * thine ever-ven’rable memory.""")

texts.append("""Pelagia most glorious, * thy corporeal loveliness * didst thou form anew in that primal dignity; *
not with bright paint or with flowers but with virtue’s embellishments * didst thou deck thyself
right fair * in the image and likeness of * thine Artificer, * while most earnestly praying and
imploring for all faithfully observing * thine ever-ven’rable memory.
""")

texts.append("""Daily pouring out the divine * alabaster jar of thy tears, * thou didst fill the Heavens with scents
exceeding sweet; * and they were offered to Christ as greatly precious and costly myrrh, * shed
with heartfelt fervency * as the sweet mystic fragrancy * of thy love for Him. * Do thou therefore
beseech Him and implore Him for all faithfully observing * thine ever-ven’rable memory.
""")

for i, text in enumerate(texts):
    prosomoiahelper.generate_prosomoia(
        text, 
        'example_1__input.byzx', 
        f'example_1__output_{i+1}.byzx')