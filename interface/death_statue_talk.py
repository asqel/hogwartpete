import pygame as py
import interface
import items



class Death_statue(interface.Gui):
    def __init__(self, player) -> None:
        self.text_idx = 0
        self.text = [
            [
            "Ô toi qui entend ma voix,",
            "écoute. Il y a longtemps,",
            "j'ai été enfermé dans une",
            "statue de terre cuite."],
            [
            "Certains me nomment la",
            "mort. Retrouve mes 3",
            "reliques. Je t'offrirai",
            "une recompense."]
            ]
        self.text_color = [
            [(0, 0, 0) , (0,0,0), (0,0,0), (0,0,0)],
            [(0, 0, 0) , (0,0,0), (0,0,0), (0,0,0)]
        ]
        self.text_len = len(self.text)
        super().__init__(self.__class__.__name__, {}, player)
        
        
    def tick(self, events: list[py.event.Event]):
        
        for i in events:
            if i.type == py.KEYDOWN:
                if i.key == py.K_e:
                    if self.text_idx < self.text_len - 1:
                        self.text_idx += 1
                    else:
                        self.player.close_gui()
                    
            
    def draw(self, screen):
        interface.draw_4_line(screen , self.text[self.text_idx], self.text_color[self.text_idx])
                    




interface.registerGui(Death_statue)

"""

"""

