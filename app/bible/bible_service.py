import random

from app.bible.models import BibleVerse


class BibleService:
    """
    Sementara menggunakan daftar ayat lokal.

    Nanti sangat mudah diganti menjadi API SABDA
    tanpa mengubah kode lain.
    """

    VERSES = [

        BibleVerse(
            reference="Yohanes 3:16",
            text="Karena begitu besar kasih Allah akan dunia ini sehingga Ia telah mengaruniakan Anak-Nya yang tunggal...",
            translation="TB"
        ),

        BibleVerse(
            reference="Mazmur 23:1",
            text="TUHAN adalah gembalaku, takkan kekurangan aku.",
            translation="TB"
        ),

        BibleVerse(
            reference="Yesaya 41:10",
            text="Jangan takut, sebab Aku menyertai engkau.",
            translation="TB"
        ),

        BibleVerse(
            reference="Roma 8:28",
            text="Allah turut bekerja dalam segala sesuatu untuk mendatangkan kebaikan.",
            translation="TB"
        ),

        BibleVerse(
            reference="Filipi 4:13",
            text="Segala perkara dapat kutanggung di dalam Dia yang memberi kekuatan kepadaku.",
            translation="TB"
        ),

    ]

    def random(self) -> BibleVerse:

        return random.choice(self.VERSES)

    def get(self, reference: str) -> BibleVerse | None:

        for verse in self.VERSES:

            if verse.reference.lower() == reference.lower():

                return verse

        return None
