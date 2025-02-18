import os, whisper

class Audio_to_text():
    def __init__(self):
        self.__audios_path = os.path.join(os.getcwd(),"audios")
        self.__transcripts_path = os.path.join(os.getcwd(),"transcripts")
        self.audios = self._fetch_audios()
        self.__model = whisper.load_model("large")

    def _fetch_audios(self) -> list:
        return os.listdir(self.__audios_path)
    
    def transcribe(self, file=None) -> None:
        if file:
            assert(os.path.exists(os.path.join(self.__audios_path,file)))
            print(f"Transcribiendo {file}...")
            result = self.__model.transcribe(os.path.join(self.__audios_path,file))
            self.text_to_file(result["text"],file[:-4])
            return
        l = len(self.audios)
        for i, aud in enumerate(self.audios, 1):
            print(f"\rTranscribiendo {aud}  [{i}/{l}]...")
            result = self.__model.transcribe(os.path.join(self.__audios_path,aud))
            self.text_to_file(result["text"],aud[:-4])

    def text_to_file(self, text:str, title=None) -> None:
        if not title: title = text[:8]
        with open(os.path.join(self.__transcripts_path,f"{title}.txt"), "w", encoding="UTF-8") as file:
            file.write(text)
            file.close()

if __name__ == "__main__":
    a = Audio_to_text()
    while True:
        act = int(input("0) Exit \n1) Translate all \n2) Select file \n -> "))
        if act == 0: break
        if act == 1: a.transcribe()
        if act == 2:
            print(a.audios)
            file = input("Ingresa el nombre del archivo: ")
            a.transcribe(file)