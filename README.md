Integration With Telegram and Wazuh SAS

To test, just execute python3 telegram.py alerts.json <alerts.json> wazuh file example

don´t forget to change -> TELEGRAM_TOKEN and TELEGRAM_CHAT_ID. Visit @BotFather telegram to more details. 

Wazuh TAG Integration

****<integration>
****<name>telegram.py</name>
****<level>10</level>
****<alert_format>json</alert_format>
****</integration> 
