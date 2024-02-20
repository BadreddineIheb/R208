class voiture :
    def __init__(self, marque="Inconnue" , modele="Inconnue" , puissancefiscale=0 , couleur='blanc') : 
        self.__marque = marque
        self.__modele = modele
        self.__puissancefiscale = puissancefiscale
        self.__couleur = couleur
        self.__options = []
    def get_marque(self):
        return self.__marque
    def set_marque(self,marque):
        self.__marque = marque

    def get_modele(self):
        return self.__modele
    def set_modele(self,modele):
        self.__modele = modele

    def get_puissancefiscale(self):
        return self.__puissancefiscale
    def set_puissancefiscale(self,puissancefiscale) :
        self.__puissancefiscale = puissancefiscale

    def get_couleur(self):
        return self.__couleur
    def set_couleur(self,couleur):
        self.__couleur = couleur
    
    def affichage (self):
        print(self.__marque)
        print(self.__modele)
        print(self.__puissancefiscale)
        print(self.__couleur)

    def affichage_get(self):
        print(self.get_marque())
        print(self.get_modele())
        print(self.get_puissancefiscale())
        print(self.get_couleur())


    def get_options(self):
        return self.__options

    def set_options(self, options):
        self.__options = options

    def ajouter_option(self, opt):
        self.__options.append(opt)

    def supprimer_option(self, opt):
        if opt in self.__options:
            self.__options.remove(opt)
        else:
            print(f"L'option {opt} n'est pas présente dans la liste.")

    def is_option_present(self, opt):
        return opt in self.__options

    def __str__(self):
        options_str = ", ".join(self.__options)
        return f"Voici les caractéristiques de cette voiture:\n- Marque : {self.get_marque()}\n- Modele : {self.get_modele()}\n- Couleur : {self.get_couleur()}\n- Puissance : {self.get_puissancefiscale()}\n- Options : {options_str}"