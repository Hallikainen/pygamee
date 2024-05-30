import pygame
import random
import os
from screeninfo import get_monitors
import csv

class Robojump:
    def __init__(self):
        pygame.init()
        #poista kommentointi jos haluat että peli aukeaa toiselle näytölle 
        # naytot = get_monitors()
        # toinen_naytto = naytot[1]
        # x = toinen_naytto.x
        # y = toinen_naytto.y
        # os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"
        
        #näyttömäärittely sekä otsikko
        self.naytto = pygame.display.set_mode((640, 480))
        self.nayton_leveys = 800
        self.nayton_korkeus = 600
        pygame.display.set_caption("RoboJump 3000")
        
        #parametrien alustus
        self.kuolemat = 0
        self.tekstiruutu = True
        self.intro = True
        self.valikuolema = False
        self.loppukuolema = False
        self.morko_osuma = False
        self.tippuminen = False
        self.pelaa = True
        self.pisteet = 0
        
        #ladataan kuvat
        self.lataa_kuvat()
        
        #pisteet
        self.max_pisteet = 0
        self.pisteet = 0
        self.uusi_ennatys = False
        
        #pelin toinen alustus
        self.valialustus()

    def valialustus(self):
        #alustetaan parametrit
        self.vakio_parametrit()
        self.muuttuvat_parametrit()   
        
        #avataan tekstiruutu
        if self.tekstiruutu:
            self.silmukka()
        
        #pelaamaan
        elif self.pelaa:
            #luodaan tasot
            self.luodaan_tasot()
            #luodaan kolikot
            self.luodaan_kolikot()
            #luodaan morot
            self.luodaan_morot()
            #kello
            self.clock = pygame.time.Clock()
            #silmukkaan
            self.silmukka()

    def ennatykset(self):
        #lue ennätykset
        with open("/Users/vapaaeero/Documents/opinnot/opinnot/ohjelmoinnin-perusteet/tmcdata/mooc-ohjelmointi-2024/osa14-01_pelin_palautus/src/ennatys.txt", "r") as tiedosto:
            ennatys = tiedosto.read()
            if len(ennatys) != 0:
                ennatys = int(ennatys)
            else:
                ennatys = 0
            pisteet = self.max_pisteet
            #rikkoutuiko ennätys?
            if pisteet > ennatys:
                self.uusi_ennatys = True
                ennatys_rivi = str(pisteet)
            
                #tallennetaan uusi ennätys
                with open("/Users/vapaaeero/Documents/opinnot/opinnot/ohjelmoinnin-perusteet/tmcdata/mooc-ohjelmointi-2024/osa14-01_pelin_palautus/src/ennatys.txt", "w") as tiedosto:
                    tiedosto.write(ennatys_rivi)

    def vakio_parametrit(self):
        #tasot
        #lähtötason koordinaatit
        self.lt_x1 = 20
        self.lt_x2 = 200
        self.lt_y = 480
        
        #tasojen nopeus
        self.tasot_v = 1.5
        
        #alkukoordinaatit
        self.robo_x = 320
        self.robo_y = 230-self.robo_height
        
        #nopeudet 
        self.robo_v_y = 0
        self.robo_v_x = 4
        self.painovoima = 0.5
        self.hyppynopeus = -11
        
        #morot
        self.morko_v = 2   
        
        #välitekstit
        self.aloitusaika = pygame.time.get_ticks()
        self.tekstiaika = 2000

    def muuttuvat_parametrit(self):
        #robotin ohjailu
        self.hyppaa = False
        self.oikealle = False
        self.vasemmalle = False
        
        #muut
        self.elamat = 3 - self.kuolemat

    def lataa_kuvat(self):
        #robo
        self.robo = pygame.image.load("robo.png")
        
        #korkeus ja leveys 
        self.robo_height = self.robo.get_height()
        self.robo_width = self.robo.get_width()
        
        #muut kuvat
        self.kolikko = pygame.image.load("kolikko.png")
        self.morko = pygame.image.load("hirvio.png")
        self.elama = pygame.transform.scale(self.robo, (self.robo_width/3, self.robo_height/3))

    def luodaan_tasot(self):
        self.tasot = []
        y = 200
        eka_taso = {"x1" : 0, "x2" : 640, "y" : 240, "n" : 0}
        self.tasot.append(eka_taso)
        for i in range(1, 500):
            if i % 2 != 0:
                x1 = 0
                x2 = 300 + random.randint(-50, 50)
            if i % 2 == 0:
                x1 = 400 + random.randint(-50, 50)
                x2 = 640 
            y = y - random.randint(40, 100)
            self.tasot.append({"x1" : x1, "x2" : x2, "y" : y, "n" : i})

    def luodaan_kolikot(self):
        self.kolikot = []
        i = 1
        for taso in self.tasot:
            if i % 3 == 0:
                kol_x = taso["x1"] + random.randint(40, 80)
                kol_y = taso["y"] + random.randint(5, 30)
                self.kolikot.append({"x" : kol_x, "y" : kol_y})
                if i % 5 == 0:
                    kol_x2 = kol_x + 40
                    kol_y2 = kol_y
                    self.kolikot.append({"x" : kol_x2, "y" : kol_y2})
                if i % 10 == 0:
                    kol_x3 = kol_x2 + 40
                    kol_y3 = kol_y
                    self.kolikot.append({"x" : kol_x3, "y" : kol_y3})
            i += 1

    def luodaan_morot(self):
        self.morot = []
        y = 0
        for i in range(1,500):
            x = random.randint(40, 600)
            y = y - random.randint(400, 1000)
            self.morot.append({"x" : x, "y" : y})

    def silmukka(self):
        #pelaamaan 
        while self.pelaa and not self.tekstiruutu:
            self.tasot_liikkuu()
            self.kolikot_liikkuu()
            self.morot_liikkuu()
            self.tutki_tapahtumat()
            self.robo_liikkuu()
            self.piirra_naytto()
        
        #tekstiruutuun
        while self.tekstiruutu:
            self.tutki_tapahtumat()
            self.piirra_naytto()

    def tasot_liikkuu(self):
        #määritetään nopeus
        for taso in self.tasot:
            if taso["n"] > 30 and taso["y"] > 0:
                self.tasot_v = 2
            if taso["n"] > 60 and taso["y"] > 0:
                self.tasot_v = 2.5
            if taso["n"] > 90 and taso["y"] > 0:
                self.tasot_v = 3
        
        #siirretään tasoja        
        for taso in self.tasot:
            taso["y"] += self.tasot_v

    def kolikot_liikkuu(self):
        for kol in self.kolikot:
            if kol["y"] < 500:
                kol["y"] += self.tasot_v
            
            #x-suuntainen kolikko-osuma
            if abs(self.robo_x - kol["x"]) < self.robo_width/2 + 20:
                
                #y-suuntainen kolikko-osuma
                if abs(self.robo_y + 20 - kol["y"]) < self.robo_width + 20:
                    kol["y"] += 500
                    self.pisteet += 1
    
    def morot_liikkuu(self):
        for morko in self.morot:
            if morko["y"] < 500:
                morko["y"] += self.tasot_v + random.uniform(0.5, 6)
            
            #x-suuntainen mörköosuma
            if abs(self.robo_x - morko["x"]) < self.robo_width/2 + 20:
                
                #y-suuntainen mörköosuma
                if abs(self.robo_y + 20 - morko["y"]) < self.robo_width + 20:
                    self.kuolemat += 1
                    self.valikuolema = True
                    self.morko_osuma = True
                    self.tekstiruutu = True
                    if self.kuolemat >= 3:
                        self.loppukuolema = True
                        self.valikuolema = False
                    self.valialustus()
                    
    def tutki_tapahtumat(self):
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit() 

            #robon liikkeeseen vaikuttavat tapahtumat
            if tapahtuma.type == pygame.KEYDOWN and self.pelaa:
                if tapahtuma.key == pygame.K_UP and not self.hyppaa:
                    self.robo_v_y = self.hyppynopeus
                    self.hyppaa = True
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = True
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = True
            
            if tapahtuma.type == pygame.KEYUP:
                if tapahtuma.key == pygame.K_RIGHT:
                    self.oikealle = False
                if tapahtuma.key == pygame.K_LEFT:
                    self.vasemmalle = False           
            
            #loppuruudun valikot (restart tai exit)
            if tapahtuma.type == pygame.KEYDOWN and self.loppukuolema:
                if tapahtuma.key == pygame.K_r:
                    self.loppukuolema = False
                    self.pelaa = True
                    self.__init__()
            if tapahtuma.type == pygame.KEYDOWN and self.loppukuolema:
                if tapahtuma.key == pygame.K_e:
                    exit()
                    
        pygame.time.Clock().tick(60)

    def robo_liikkuu(self):
        #robon hyppy
        self.robo_v_y += self.painovoima
        self.robo_y += self.robo_v_y
        
        #robo sivuille 
        if self.oikealle == True:
            self.robo_x += self.robo_v_x
        if self.vasemmalle == True:
            self.robo_x -= self.robo_v_x
        self.pysy_tasolla()
        
        #robo tippuu
        if self.robo_y > 480:
            self.kuolemat += 1
            self.valikuolema = True
            self.tippuminen = True
            self.tekstiruutu = True
            if self.kuolemat >= 3:
                self.pelaa = False
                self.valikuolema = False
                self.loppukuolema = True
            self.valialustus()
         
    def pysy_tasolla(self):
        for taso in self.tasot:
            
            #onko robotti tason yläpuolella ja putoaako se
            if abs(taso["y"] - (self.robo_y + self.robo_height)) < 5:
                
                #osuuko se tason x-koordinaattien väliin
                if taso["x1"] - self.robo_width < self.robo_x < taso["x2"] and self.robo_v_y > 0: 
                    self.robo_y = taso["y"] - self.robo_height
                    self.robo_v_y = 0
                    self.hyppaa = False
    
    def piirra_naytto(self):
        if self.pelaa and self.tekstiruutu is False:
            
            #tausta
            self.naytto.fill((51, 255, 255))
            
            #piirrä robo
            self.naytto.blit(self.robo, (self.robo_x, self.robo_y))
            
            #piirrä tasot
            for taso in self.tasot:
                pygame.draw.line(self.naytto, (255, 51, 255), (taso["x1"], taso["y"]), (taso["x2"], taso["y"]), 5)
            
            #piirrä kolikot
            i = 1
            for kol in self.kolikot:
                self.naytto.blit(self.kolikko, (kol["x"], kol["y"]))
                i += 1
            
            #piirrä pisteet
            fontti = pygame.font.SysFont('Courier New', 22)
            teksti = fontti.render(f"pisteet: {self.pisteet}", True, (0, 0, 0))
            self.naytto.blit(teksti, (490, 20))
            
            #piirra möröt
            for morko in self.morot:
                self.naytto.blit(self.morko, (morko["x"], morko["y"]))
            
            #piirrä elamat
            for i in range(self.elamat):
                self.naytto.blit(self.elama, (20+i*20, 20)) 
            
            pygame.display.flip()

        #piirrä tekstiruudut
        if self.tekstiruutu:
            aika_nyt = pygame.time.get_ticks()
            kulunut_aika = aika_nyt - self.aloitusaika
            
            #introtekstit
            if self.intro:
                fontti = pygame.font.SysFont('Courier New', 24)
                teksti = fontti.render("RoboJump 3000 käynnistyy...", True, (20, 0, 20))
                teksti_positio = teksti.get_rect(center=(320, 240))
                if kulunut_aika < self.tekstiaika:
                    self.naytto.fill((160, 160, 160))
                    self.naytto.blit(teksti, teksti_positio)
                else:
                    self.tekstiruutu = False
                    self.intro = False
                    self.valialustus()
            
            #välikuolema-tekstit
            elif self.valikuolema:
                fontti = pygame.font.SysFont('Courier New', 24)
                
                #mörköosuma
                if self.morko_osuma:
                    teksti = f"Osuit mörköön! Elämiä jäljellä: {self.elamat}"
                    teksti_muotoilu = fontti.render(teksti, True, (0, 0, 0))
                
                #tippuminen
                if self.tippuminen:
                    teksti = f"Tipahdit! Elämiä jäljellä: {self.elamat}"
                    teksti_muotoilu = fontti.render(teksti, True, (0, 0, 0))
                teksti_positio = teksti_muotoilu.get_rect(center=(320, 240))
                if kulunut_aika < self.tekstiaika:
                    self.naytto.blit(teksti_muotoilu, teksti_positio)
                else:
                    self.tekstiruutu = False
                    self.valikuolema = False
                    self.morko_osuma = False
                    self.tippuminen = False 
                    self.valialustus()

            #loppukuolema-tekstit
            elif self.loppukuolema:
                fontti = pygame.font.SysFont('Courier New', 24)
                teksti = fontti.render('Peli päättyi!', True, (0, 0, 0))
                teksti_positio = teksti.get_rect(center=(320, 240))
                self.naytto.blit(teksti, teksti_positio)
                self.ennatykset()
                if self.uusi_ennatys:
                    teksti = fontti.render(f"Uusi ennätys: {self.max_pisteet}", True, (0, 0, 0))
                    teksti_positio = teksti.get_rect(center=(320, 280))
                    self.naytto.blit(teksti, teksti_positio)

                #restart
                fontti = pygame.font.SysFont('Courier New', 18)
                teksti = fontti.render('Pelaa uudestaan (R)', True, (0, 0, 0))
                self.naytto.blit(teksti, (30, 440))

                #exit
                fontti = pygame.font.SysFont('Courier New', 18)
                teksti = fontti.render('Lopeta (E)', True, (0, 0, 0))
                self.naytto.blit(teksti, (500, 440))

            pygame.display.flip()

if __name__ == "__main__":
    Robojump()









