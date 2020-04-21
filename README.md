# vk-covid
Изменения смайлика возле фамилии в ВК по таймеру 

# Установка
<code>apt update && apt upgrade</code><br>
<code>apt install git</code><br>
<code>git clone https://github.com/FSystem88/vk-covid</code><br>
<code>cd vk-covid</code><br>
<code>./install.sh</code><br>
<br><br><br>
• е каждый токен подходит. <br>
• Чтобы получить нужный токен перейдите на официальную страницу ВК:<br>
<a href="https://vk.com/covid19">https://vk.com/covid19</a><br>
• Нажмите на клавиатуре F12 и на появившейся панеле перейдите во вкладку Network (обычно идет после вкладок Elements-Console-!Network!).<br>
• Далее нажмите на любой смайлик, можно на несколько.<br>
• Потом нажмите на клавиатуре Ctrl+F и вставьте туда <b>users.setCovidStatus</b><br>
• У вас высветится кое что желтым, нажимаете на это и перед вами будет длинная ссылка<br>
• Псле слова <b>access_token=</b> идёт ваш длинный токен аж до слова <b>&request_id=</b><br>
• Вуаля, нужный токен найден!
