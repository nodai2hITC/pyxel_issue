import pyxel

pyxel.init(160, 120, fps=5)

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(0,  0, 'caret pressed.'    , 1 + 6*pyxel.btn(pyxel.KEY_CARET))
    pyxel.text(0, 10, 'atmark pressed.'   , 1 + 6*pyxel.btn(pyxel.KEY_AT))
    pyxel.text(0, 20, 'semicolon pressed.', 1 + 6*pyxel.btn(pyxel.KEY_SEMICOLON))
    pyxel.text(0, 30, 'colon pressed.'    , 1 + 6*pyxel.btn(pyxel.KEY_COLON))
    pyxel.text(0, 50, str(pyxel.input_keys), 7)

pyxel.run(update, draw)
