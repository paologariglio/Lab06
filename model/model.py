from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        try:
            cnx = get_connection()
            strumenti = []
            cursore = cnx.cursor(dictionary=True) #è il cursore che scorre nel database
            query = f"""SELECT * 
                        FROM strumento"""
            cursore.execute(query)

            for riga in cursore.fetchall():
                s = Strumento(riga[0],riga[1],riga[2],riga[3],riga[4],riga[5])
                strumenti.append(s)

            return strumenti

        except Exception as e:
            print(f"Errore database: {e}")
            return None

        finally:
            if cnx and cnx.is_connected():
                cursore.close()
                cnx.close()



    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        try:
            cnx = get_connection()
            strumenti = []
            cursore = cnx.cursor(dictionary=True)  # è il cursore che scorre nel database
            query = f"""SELECT * 
                        FROM strumento
                        WHERE tipo = %s"""
            cursore.execute(query,(tipo,)) #prende il tipo che hai dato in input ed esegue la query in base a quello

            for riga in cursore.fetchall():
                s = Strumento(riga[0], riga[1], riga[2], riga[3], riga[4], riga[5])
                strumenti.append(s)

                return strumenti

        except Exception as e:
            print(f"Errore database: {e}")
            return None

        finally:
            if cnx and cnx.is_connected():
                cursore.close()
                cnx.close()
