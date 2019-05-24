*Dibuixos de la serie de Dragon ball Z, tots el drets reservats
llicència CC-BY-NC

URL dels personatges:
https://www.google.com/search?rlz=1C1CHBF_caES819ES819&biw=1400&bih=907&tbm=isch&sa=1&ei=rlnhXJQo4uaDB52LmdgJ&q=dragon+ball+z+personajes&oq=dragon+ball+z+pers&gs_l=img.1.0.0i19l2j0i30i19l8.8688.11081..13456...2.0..0.143.832.1j6......0....1..gws-wiz-img.......0i67j0j0i30j0i8i10i30.4Y8TneRtblo

URL dels paissatges:
https://www.google.com/search?rlz=1C1CHBF_caES819ES819&biw=1400&bih=858&tbm=isch&sa=1&ei=SFzhXJCuBLCFjLsP5Y6-4Aw&q=planeta+namac&oq=planeta+namac&gs_l=img.3..0i10i24.118777.123737..124119...0.0..0.461.1837.3j4j0j2j1......0....1..gws-wiz-img.......0i19.QGPgqaR87xk#imgrc=Fo6qSAKg-T9GWM:

*En el cas d'haver-hi dificultat de moure els objectes :
	Hem de tenir sempre present del refrescament continuat dels objectes en la càrrega del fitxer .img seu com principal
	handicap per obtenir una qualitat optima per el moviments d'aquest, mostra per guanyar qualitat serà de modificar els
	bucles boolean on sigui les càrregues de fitxers en els mètodes, canviar les seves posicions booleans contraries per
	només accedir-hi un cop.

*Dissenyat la part del projecte Front-page per l'usuari amb programació orientada a objectes, empleat el mètode d'encapsulació
 de les classes. Tenim una principal classe anomenada Joc, de la que el seu constructor inicialitzarem totes els atributs de 
pantalla, variables boolean,... aquesta està composta per 10 mètodes que són els següents:
		modiMides() : dissenyada per poder-hi modificar les mides dels objectes en el redimensionament de la mida de la finestre pygame amb le tecles de control F1, F2, F3 
		procesEvents() : cicle per els esdeveniments d'entrada de teclat controlat per bucle while dins del general, sortirem d'ell per un boolean negat.
 		logicaExecutar() : mètode per obtenir el valor exactes de posició d'objecte, com controlador dels atributs del marcador del joc, com el control de carregues d'imatge per nivell
		visualPantalla()
		connecSQL()
		evensRanking()
		visualRank()
		EvensMenu()
		visualMenu()
		game_over()
 A part de tenir la nostre super classe principal 'Joc', tenim 5 classes més en dependència de la principal són les següents:
		class: Jugador1()
		class: Jugador2()
		class: Text1()
		class: carregaImg()
		class: Boladrac()