# -*- coding: utf-8 -*-
"""File generated according to PWSlot61/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot61.Ui_PWSlot61 import Ui_PWSlot61


class Gen_PWSlot61(Ui_PWSlot61):
    def setupUi(self, PWSlot61):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot61.setupUi(self, PWSlot61)
        # Setup of in_W0
        txt = self.tr("""Pole top width""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Pole top width""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Pole top width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Pole top width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr("""Pole bottom width""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Pole bottom width""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Pole top height""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Pole top height""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""Pole intermediate height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Pole intermediate height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Pole bottom height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Pole bottom height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""Edge Distance Ploe-coil """)
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Edge Distance Ploe-coil """)
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_H3
        txt = self.tr("""Top Distance Ploe-coil """)
        self.in_H3.setWhatsThis(txt)
        self.in_H3.setToolTip(txt)

        # Setup of lf_H3
        self.lf_H3.validator().setBottom(0)
        txt = self.tr("""Top Distance Ploe-coil """)
        self.lf_H3.setWhatsThis(txt)
        self.lf_H3.setToolTip(txt)

        # Setup of in_H4
        txt = self.tr("""Bottom Distance Ploe-coil """)
        self.in_H4.setWhatsThis(txt)
        self.in_H4.setToolTip(txt)

        # Setup of lf_H4
        self.lf_H4.validator().setBottom(0)
        txt = self.tr("""Bottom Distance Ploe-coil """)
        self.lf_H4.setWhatsThis(txt)
        self.lf_H4.setToolTip(txt)
