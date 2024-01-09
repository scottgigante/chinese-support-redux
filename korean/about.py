from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from aqt import mw

from ._version import __version__

CSR_GITHUB_URL = "https://github.com/scottgigante/korean-support"


def showAbout():
    dialog = QDialog(mw)

    label = QLabel()
    label.setStyleSheet("QLabel { font-size: 14px; }")

    contributors = [
        "Alex Griffin",
        "Chris Hatch",
        "Roland Sieker",
        "Thomas TEMPÉ",
        "Luo Li-Yan",
        "Scott Gigante",
        "Paul Lee",
    ]

    text = """
<div style="font-weight: bold">Korean Support v%s</div><br>
<div><span style="font-weight: bold">
    Maintainer</span>: Scott Gigante &lt;scottgigante@gmail.com&gt;</div>
<div><span style="font-weight: bold">Contributors</span>: %s</div>
<div><span style="font-weight: bold">Website</span>: <a href="%s">%s</a></div>
<div style="font-size: 12px">
    <br>Based on the Chinese Support add-on by Thomas TEMPÉ and many others.
    <br>If your name is missing from here, please open an issue on GitHub.
</div>
""" % (
        __version__,
        ", ".join(contributors),
        CSR_GITHUB_URL,
        CSR_GITHUB_URL,
    )

    label.setText(text)
    label.setOpenExternalLinks(True)

    buttonBox = QDialogButtonBox(QDialogButtonBox.Ok)
    buttonBox.accepted.connect(dialog.accept)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(buttonBox)

    dialog.setLayout(layout)
    dialog.setWindowTitle("About")
    dialog.exec_()
