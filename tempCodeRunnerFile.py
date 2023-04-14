img = Image.open(r"images\background.jpg")
        img = img.resize((1366, 768), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1366, height=768)