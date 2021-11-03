# "font: 14pt \"Webdings\";" \

def button_generic():
    sheet = "QPushButton{background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, " \
            "y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));border-radius: 10px;" \
            "padding: 5px;" \
            "color: rgb(255, 255, 255);" \
            "font: 11pt;" \
            "border-bottom: 2px outset black;}" \
            "QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 0 inset black;}" \
            "QPushButton:hover{background-color:#4000FF;}"
    return sheet


def button_browser():
    sheet = "QPushButton{background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, " \
            "y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));border-radius: 10px;" \
            "padding: 2px;" \
            "color: rgb(255, 255, 255);" \
            "font: 6pt;" \
            "border-bottom: 2px outset black;}" \
            "QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 0 inset black;}" \
            "QPushButton:hover{background-color:#4000FF;}"
    return sheet


####################################################################################
def input_generic():
    background = "background-color: rgb(255, 255, 255);\n" \
                 "font: 10pt \"Arial\";\n" \
                 "border-radius: 6px;\npadding: 6px;"
    return background


def input_browser():
    background = "background-color: rgb(255, 255, 255);\n" \
                 "font: 10pt \"Arial\";\n" \
                 "border-radius: 6px;\npadding: 6px;"
    return background


####################################################################################
def background_generic():
    background = "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, " \
                 "stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));}"
    return background
