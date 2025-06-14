import customtkinter as ctk
import tkinter as tk 
import os 

from .password_analyzer import analyze_password_strength
from .breach_checker import check_password_breach, get_breach_details_placeholder
from .password_generator import generate_secure_password, generate_passphrase

class PasswordGuardianApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Password Guardian")
        self.geometry("850x700")
        ctk.set_appearance_mode("System") 
        ctk.set_default_color_theme("blue") 

        self.set_window_icon()
        self.tabview = ctk.CTkTabview(self)
        self.tabview.pack(pady=20, padx=20, fill="both", expand=True)

        self.tabview.add("Analisar Senha")
        self.tabview.add("Verificar Vazamento")
        self.tabview.add("Gerar Senha")
        self.tabview.add("Dicas de Segurança")
        self.tabview.add("Sobre")

        self.create_analyze_tab()
        self.create_breach_tab()
        self.create_generate_tab()
        self.create_tips_tab()
        self.create_about_tab()

        self.after(100, self._configure_text_tags)

    def _configure_text_tags(self):
        pass 

    def set_window_icon(self):
        icon_path_ico = os.path.join("assets", "kali_icon.ico")
        icon_path_png = os.path.join("assets", "kali_icon.png")

        try:
            if os.name == 'nt' and os.path.exists(icon_path_ico): 
                self.iconbitmap(icon_path_ico)
            elif os.path.exists(icon_path_png): 
                photo = tk.PhotoImage(file=icon_path_png)
                self.wm_iconphoto(True, photo)
            else:
                print(f"Aviso: Arquivo de ícone não encontrado em '{icon_path_ico}' ou '{icon_path_png}'.")
        except Exception as e:
            print(f"Erro ao definir o ícone da janela: {e}")


    def create_analyze_tab(self):
        frame = self.tabview.tab("Analisar Senha")
        frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text="Insira a senha para análise:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20,5))
        self.password_entry_analyze = ctk.CTkEntry(frame, width=350, show="*", font=ctk.CTkFont(size=13))
        self.password_entry_analyze.pack(pady=5)

        ctk.CTkButton(frame, text="Analisar Senha", command=self.analyze_password, font=ctk.CTkFont(size=14, weight="bold")).pack(pady=15)

        ctk.CTkLabel(frame, text="Resultado da Análise:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10,0))
        self.strength_label = ctk.CTkLabel(frame, text="", font=ctk.CTkFont(size=18, weight="bold"))
        self.strength_label.pack(pady=5)
        self.feedback_text = ctk.CTkTextbox(frame, width=500, height=180, activate_scrollbars=True, wrap="word", font=ctk.CTkFont(size=12))
        self.feedback_text.pack(pady=10)
        self.feedback_text.configure(state="disabled")

    def analyze_password(self):
        password = self.password_entry_analyze.get()
        if not password:
            self.strength_label.configure(text="🚫 Por favor, insira uma senha para analisar.")
            self.feedback_text.configure(state="normal")
            self.feedback_text.delete("1.0", "end")
            self.feedback_text.configure(state="disabled")
            return

        result = analyze_password_strength(password)
        self.strength_label.configure(text=f"Força da Senha: {result['strength']} (Score: {result['score']})")

        self.feedback_text.configure(state="normal")
        self.feedback_text.delete("1.0", "end")
        self.feedback_text.insert("end", "Recomendações:\n", "bold") 
        for f in result['feedback']:
            self.feedback_text.insert("end", f"• {f}\n")
        self.feedback_text.configure(state="disabled")


    def create_breach_tab(self):
        frame = self.tabview.tab("Verificar Vazamento")
        frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text="Insira a senha para verificar vazamentos:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20,5))
        self.password_entry_breach = ctk.CTkEntry(frame, width=350, show="*", font=ctk.CTkFont(size=13))
        self.password_entry_breach.pack(pady=5)

        ctk.CTkButton(frame, text="Verificar Vazamento", command=self.check_breach, font=ctk.CTkFont(size=14, weight="bold")).pack(pady=15)

        ctk.CTkLabel(frame, text="Resultados da Verificação:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10,0))
        self.breach_results_text = ctk.CTkTextbox(frame, width=550, height=250, activate_scrollbars=True, wrap="word", font=ctk.CTkFont(size=12))
        self.breach_results_text.pack(pady=10)
        self.breach_results_text.configure(state="disabled")

    def check_breach(self):
        password = self.password_entry_breach.get()
        if not password:
            self.breach_results_text.configure(state="normal")
            self.breach_results_text.delete("1.0", "end")
            self.breach_results_text.insert("end", "🚫 Por favor, insira uma senha para verificar.\n")
            self.breach_results_text.configure(state="disabled")
            return

        self.breach_results_text.configure(state="normal")
        self.breach_results_text.delete("1.0", "end")
        self.breach_results_text.insert("end", "Verificando vazamentos... Isso pode levar um momento.\n\n")
        self.breach_results_text.configure(state="disabled")
        self.update_idletasks() 

        breaches = check_password_breach(password)

        self.breach_results_text.configure(state="normal")
        self.breach_results_text.delete("1.0", "end")

        if breaches is None:
            self.breach_results_text.insert("end", "❌ Erro ao conectar ao serviço de verificação de vazamentos.\nVerifique sua conexão com a internet e tente novamente mais tarde.\n")
        elif breaches:
            self.breach_results_text.insert("end", f"🚨 ALERTA: Senha ENCONTRADA em vazamentos conhecidos! 🚨\n", "alert_header")
            for b in breaches:
                self.breach_results_text.insert("end", f"  • Exposta {b['count']} vezes.\n", "bullet")
            self.breach_results_text.insert("end", "\n❗ RECOMENDAÇÃO URGENTE: Mude esta senha IMEDIATAMENTE em TODOS os locais onde a utilizou. Utilize uma senha forte e única para cada serviço.\n", "bold_warning")
            self.breach_results_text.insert("end", get_breach_details_placeholder() + "\n")
        else:
            self.breach_results_text.insert("end", "✅ Ótimo! Sua senha NÃO foi encontrada em vazamentos públicos conhecidos.\n\n", "success_header")
            self.breach_results_text.insert("end", "Lembre-se: Isso não garante 100% de segurança. Sempre use senhas fortes e únicas para cada conta e ative a Autenticação de Dois Fatores (2FA).\n")

        self.breach_results_text.configure(state="disabled")

        self.breach_results_text.tag_config("alert_header", foreground="red", font=ctk.CTkFont(size=14, weight="bold"))
        self.breach_results_text.tag_config("success_header", foreground="green", font=ctk.CTkFont(size=14, weight="bold"))
        self.breach_results_text.tag_config("bold_warning", font=ctk.CTkFont(size=12, weight="bold"))
        self.breach_results_text.tag_config("bullet", lmargin1=10, lmargin2=20) # Indentação

    def create_generate_tab(self):
        frame = self.tabview.tab("Gerar Senha")
        frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(frame, text="Opções de Geração de Senha:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20,5))

        self.length_label = ctk.CTkLabel(frame, text=f"Comprimento da Senha: 16", font=ctk.CTkFont(size=12))
        self.length_label.pack(pady=5)
        self.length_slider = ctk.CTkSlider(frame, from_=8, to=32, command=self.update_length_label, width=300)
        self.length_slider.set(16)
        self.length_slider.pack(pady=5)

        self.uppercase_var = ctk.BooleanVar(value=True)
        self.lowercase_var = ctk.BooleanVar(value=True)
        self.digits_var = ctk.BooleanVar(value=True)
        self.special_var = ctk.BooleanVar(value=True)

        ctk.CTkCheckBox(frame, text="Incluir Maiúsculas (A-Z)", variable=self.uppercase_var, font=ctk.CTkFont(size=12)).pack(anchor="w", padx=150, pady=2)
        ctk.CTkCheckBox(frame, text="Incluir Minúsculas (a-z)", variable=self.lowercase_var, font=ctk.CTkFont(size=12)).pack(anchor="w", padx=150, pady=2)
        ctk.CTkCheckBox(frame, text="Incluir Números (0-9)", variable=self.digits_var, font=ctk.CTkFont(size=12)).pack(anchor="w", padx=150, pady=2)
        ctk.CTkCheckBox(frame, text="Incluir Caracteres Especiais (!@#$)", variable=self.special_var, font=ctk.CTkFont(size=12)).pack(anchor="w", padx=150, pady=2)

        ctk.CTkButton(frame, text="Gerar Senha Segura", command=self.generate_password, font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(20,5))
        ctk.CTkButton(frame, text="Gerar Frase-Senha (Diceware)", command=self.generate_passphrase, font=ctk.CTkFont(size=14, weight="bold")).pack(pady=5)

        ctk.CTkLabel(frame, text="Senha Gerada:", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10,0))
        self.generated_password_entry = ctk.CTkEntry(frame, width=400, font=ctk.CTkFont(size=13))
        self.generated_password_entry.pack(pady=10)
        ctk.CTkButton(frame, text="Copiar para Área de Transferência", command=self.copy_password, font=ctk.CTkFont(size=12)).pack(pady=5)

    def update_length_label(self, value):
        self.length_label.configure(text=f"Comprimento da Senha: {int(value)}")

    def generate_password(self):
        length = int(self.length_slider.get())
        try:
            new_password = generate_secure_password(
                length=length,
                use_uppercase=self.uppercase_var.get(),
                use_lowercase=self.lowercase_var.get(),
                use_digits=self.digits_var.get(),
                use_special=self.special_var.get()
            )
            self.generated_password_entry.delete(0, "end")
            self.generated_password_entry.insert(0, new_password)
        except ValueError as e:
            self.generated_password_entry.delete(0, "end")
            self.generated_password_entry.insert(0, str(e))

    def generate_passphrase(self):
        try:
            num_words = 4 
            new_passphrase = generate_passphrase(num_words=num_words)
            self.generated_password_entry.delete(0, "end")
            self.generated_password_entry.insert(0, new_passphrase)
        except ValueError as e:
            self.generated_password_entry.delete(0, "end")
            self.generated_password_entry.insert(0, str(e))

    def copy_password(self):
        password = self.generated_password_entry.get()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            copied_label = ctk.CTkLabel(self, text="Copiado para a área de transferência!", font=ctk.CTkFont(size=12))
            copied_label.place(relx=0.5, rely=0.95, anchor="center")
            self.after(2000, copied_label.destroy)


    def create_tips_tab(self):
        frame = self.tabview.tab("Dicas de Segurança")
        frame.columnconfigure(0, weight=1)

        tips_textbox = ctk.CTkTextbox(frame, width=700, height=500, activate_scrollbars=True, wrap="word")
        tips_textbox.pack(pady=10, padx=10, fill="both", expand=True)

        textbox_internal = tips_textbox._textbox

        textbox_internal.tag_config("h2", font=("Roboto", 18, "bold"), spacing3=10, foreground="#007bff") 
        textbox_internal.tag_config("h3", font=("Roboto", 15, "bold"), spacing3=5, foreground="#17a2b8") 
        textbox_internal.tag_config("bold", font=("Roboto", 12, "bold"))
        textbox_internal.tag_config("bullet_point", lmargin1=25, lmargin2=40, font=("Roboto", 12)) 
        textbox_internal.tag_config("header_icon", font=("Roboto", 18, "bold"), foreground="green") 

        textbox_internal.insert("end", " Dicas Essenciais de Segurança de Senhas\n\n", "h2")

        textbox_internal.insert("end", " ✅ Criação de Senhas Fortes:\n", "h3")
        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Use Senhas Únicas: ", "bold")
        textbox_internal.insert("end", "Nunca reutilize senhas em diferentes serviços. Uma senha comprometida afeta todas as contas.\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Comprimento é Poder: ", "bold")
        textbox_internal.insert("end", "Mínimo de 12-16 caracteres é um bom começo. Quanto mais longa, mais segura.\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Diversidade de Caracteres: ", "bold")
        textbox_internal.insert("end", "Combine letras maiúsculas (A-Z), minúsculas (a-z), números (0-9) e caracteres especiais (!@#$%&*).\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Evite o Óbvio: ", "bold")
        textbox_internal.insert("end", "Não use informações pessoais fáceis de adivinhar (nome, data de nascimento, nome do pet, etc.).\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Frases-Senha (Passphrases): ", "bold")
        textbox_internal.insert("end", "Crie frases-senha longas e memoráveis, como \"MeuCachorroDormeNaRedeVerdeCom10Coxinhas!\". São mais seguras e fáceis de lembrar.\n\n", "bullet_point")

        textbox_internal.insert("end", " 🛡️ Gerenciamento e Proteção:\n", "h3")
        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Gerenciadores de Senhas: ", "bold")
        textbox_internal.insert("end", "Use um gerenciador de senhas (Bitwarden, LastPass, 1Password) para armazenar, gerar e preencher senhas complexas de forma segura. Você só precisa lembrar de uma senha mestra.\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Autenticação de Dois Fatores (2FA/MFA): ", "bold")
        textbox_internal.insert("end", "Ative sempre que possível! Adiciona uma camada extra de segurança (ex: código do celular, aplicativo autenticador).\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Cuidado com Phishing: ", "bold")
        textbox_internal.insert("end", "Desconfie de e-mails, mensagens ou sites que pedem suas credenciais. Verifique sempre a URL e o remetente.\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Atualize seu Software: ", "bold")
        textbox_internal.insert("end", "Mantenha seu sistema operacional, navegadores e aplicativos sempre atualizados para corrigir vulnerabilidades.\n\n", "bullet_point")

        textbox_internal.insert("end", " 🚨 Em Caso de Vazamento:\n", "h3")
        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Aja Imediatamente: ", "bold")
        textbox_internal.insert("end", "Se sua senha foi vazada (verifique na aba \"Verificar Vazamento\"), mude-a imediatamente em todos os locais onde a utilizou.\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Monitore Contas: ", "bold")
        textbox_internal.insert("end", "Fique atento a atividades suspeitas em suas contas online (e-mail, redes sociais, bancos).\n", "bullet_point")

        textbox_internal.insert("end", "• ", "header_icon")
        textbox_internal.insert("end", "Considere Alerta de Crédito: ", "bold")
        textbox_internal.insert("end", "Em casos de vazamentos graves, pode ser prudente monitorar suas contas bancárias.\n", "bullet_point")

        tips_textbox.configure(state="disabled") 


    def create_about_tab(self):
        frame = self.tabview.tab("Sobre")
        frame.columnconfigure(0, weight=1)

        about_textbox = ctk.CTkTextbox(frame, width=600, height=300, activate_scrollbars=True, wrap="word")
        about_textbox.pack(pady=20, padx=20, fill="both", expand=True)

        textbox_internal = about_textbox._textbox
        textbox_internal.tag_config("h2", font=("Roboto", 20, "bold"), spacing3=15, foreground="#007bff")
        textbox_internal.tag_config("paragraph", font=("Roboto", 12), spacing3=10)
        textbox_internal.tag_config("section_header", font=("Roboto", 14, "bold"), spacing3=5, spacing1=10)
        textbox_internal.tag_config("contact_info", font=("Roboto", 12, "bold"))
        textbox_internal.tag_config("link", font=("Roboto", 12, "underline"), foreground="blue")


        textbox_internal.insert("end", " ✨ Sobre o Password Guardian\n\n", "h2")
        textbox_internal.insert("end", "Este projeto foi desenvolvido com o objetivo de ser uma ferramenta útil e educativa no campo da cibersegurança, focando em senhas. Meu intuito foi criar algo prático e acessível, que pudesse ajudar tanto a mim quanto a outros usuários a entender e melhorar a segurança de suas credenciais online.\n\n", "paragraph")
        textbox_internal.insert("end", "É um projeto de estudo pessoal, construído de forma independente, e reflete meu aprendizado e dedicação contínua à cibersegurança.\n\n", "paragraph")

        textbox_internal.insert("end", "---", "paragraph") 

        textbox_internal.insert("end", "\n\n", "paragraph") 
        textbox_internal.insert("end", "Criador:\n", "section_header")
        textbox_internal.insert("end", "Yankkj\n\n", "contact_info")

        textbox_internal.insert("end", "GitHub:\n", "section_header")
        textbox_internal.insert("end", "https://github.com/yankkj\n\n", "link") 

        textbox_internal.insert("end", "Discord:\n", "section_header")
        textbox_internal.insert("end", "imundar\n\n", "contact_info")

        textbox_internal.insert("end", "Telegram:\n", "section_header")
        textbox_internal.insert("end", "feicoes\n\n", "contact_info")

        textbox_internal.insert("end", "Agradeço por usar o Password Guardian!\n", "paragraph")

        about_textbox.configure(state="disabled") 

        copy_button = ctk.CTkButton(frame, text="Copiar Texto", command=lambda: self._copy_about_text(about_textbox.get("1.0", "end")), font=ctk.CTkFont(size=12))
        copy_button.pack(pady=10)

    def _copy_about_text(self, text_to_copy):
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)
        copied_label = ctk.CTkLabel(self, text="Texto copiado!", font=ctk.CTkFont(size=12))
        copied_label.place(relx=0.5, rely=0.95, anchor="center")
        self.after(2000, copied_label.destroy)


if __name__ == "__main__":
    app = PasswordGuardianApp()
    app.mainloop()