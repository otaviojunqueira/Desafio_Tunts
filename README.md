
# Desafio Tunts
## Português [BR]

O projeto consiste em um script em Python que automatiza a atualização de informações em uma planilha do Google Sheets. A planilha contém dados de alunos, incluindo informações como matrícula, nome, faltas e notas em avaliações. O script é capaz de realizar o cálculo da situação de cada aluno com base nas faltas e médias, atualizando automaticamente as células correspondentes na planilha.

_Principais Funcionalidades:_
--

**1- Cálculo da Situação do Aluno:**

- O script calcula a situação de cada aluno com base nas faltas e médias de avaliações.
- As situações possíveis são *"Aprovado"*, *"Exame Final"*, *"Reprovado por Falta"* e *"Reprovado por Nota"*.

**2. Cálculo de Nota para Aprovação Final:**

- Para alunos em situação de "Exame Final", isto é, que não atingiram a média para serem considerados aprovados, o script calcula e atualiza a nota necessária para aprovação.

**3-Atualização Automática na Planilha:**

- As informações atualizadas são refletidas diretamente na planilha do Google Sheets.

**4-registro de Logs no Terminal:**

- Mensagens de log são exibidas no terminal para acompanhar as operações realizadas durante a execução do script.

**5-Requisitos e Dependências:**

- O projeto requer uma conta de serviço no Google Cloud, que fornece o arquivo de credenciais **('credentials.json')**.

- Dependências incluem as bibliotecas **'gspread'** e **'pandas'**.















---
  ## Instruções para Execução da Aplicação

 **1- Configuração do Ambiente Virtual:**

- No diretório do seu projeto, abra um terminal.

- Crie um ambiente virtual com o comando:

      python -m venv venv
   
- Ative o ambiente virtual:

   -> No Windows:

      .\venv\Scripts\activate

   -> No Linux/Mac:

       source venv/bin/activate


---
**2- Instalação das Dependências:**

- Certifique-se de estar com o ambiente virtual ativado.

- Instale as dependências necessárias usando o comando:
       
       pip install -r requirements.txt

- Este comando instalará as bibliotecas **gspread**, **pandas**, e outras necessárias para o projeto.


---
**3- Configuração do Arquivo de Credenciais do Google:**

- Baixe o arquivo **'credentials.json'** do [Console de APIs do Google](https://console.cloud.google.com/apis/library?hl=pt-BR).

- Mova o arquivo **'credentials.json'** para o diretório do seu projeto
---

**4- Execução do Script Principal:**

- Execute o script principal com o seguinte comando:

       python app.py

- Aguarde até que o script seja concluído.

---

**5- Verificação dos Resultados:**

- Após a execução, verifique a planilha Google Sheets fornecida para ver as atualizações nas células correspondentes.

---


__*Observações:*__

- Certifique-se de ter uma conexão com a internet durante a execução, pois o script interage com o Google Sheets online.

- A mensagem de aviso relacionada ao Pyarrow é informativa e não afeta a execução do código.

---
# English [US]  
   
The project consists of a Python script that automates the update of information in a Google Sheets spreadsheet. The spreadsheet contains student data, including details such as enrollment number, name, absences, and scores in assessments. The script can calculate the situation of each student based on absences and averages, automatically updating the corresponding cells in the spreadsheet.


_Main Features:_
--

**1- Calculation of Student Situation:**

- The script calculates each student's situation based on absences and average assessments.
- The possible situations are *"Passed"*, *"Final Exam"*, *"Failed due to Absence"* and *"Failed due to Grade"*.

**2. Grade Calculation for Final Approval:**

- For students in a "Final Exam" situation, that is, who did not reach the average to be considered approved, the script calculates and updates the grade required for approval.

**3-Automatic Spreadsheet Update:**

-  Updated information is reflected directly in the Google Sheets spreadsheet.

**4-Log recording in the Terminal:**

- Log messages are displayed on the terminal to track operations performed during script execution.

**5-Requirements and Dependencies:**

- The project requires a service account on Google Cloud, which provides the credentials file **('credentials.json')**.

- Dependencies include the **'gspread'** and **'pandas'** libraries.
---

 ## Instructions for Executing the Application

 **1- Virtual Environment Configuration:**

- In your project directory, open a terminal.

- Create a virtual environment with the command:

      python -m venv venv
   
- Activate the virtual environment:

   -> On Windows:

      .\venv\Scripts\activate

   -> On Linux/Mac:

       source venv/bin/activate

---

**2- Installation of Dependencies:**

- Make sure you have the virtual environment activated.

- Install the necessary dependencies using the command:
       
       pip install -r requirements.txt

- This command will install the **gspread**, **pandas**, and other libraries needed for the project.


---
   
**3- Configuring the Google Credentials File:**

- Download the **'credentials.json'** file from [Google API Console](https://console.cloud.google.com/apis/library?hl=pt-BR).

- Move the **'credentials.json'** file to your project directory
---

**4- Main Script Execution:**

- Run the main script with the following command:

       python app.py

- Wait for the script to complete.

---

**5- Checking Results:**

- After execution, check the provided Google Sheets spreadsheet for updates to the corresponding cells.

---


__*Comments:*__

- Make sure you have an internet connection while running, as the script interacts with Google Sheets online.

- Pyarrow-related warning message is informational and does not affect code execution.

---

