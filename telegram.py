#!/usr/bin/env python3
import json
import requests
import sys

TELEGRAM_TOKEN = "INSIRA SEU TOKEN"
TELEGRAM_CHAT_ID = "INSIRA SEU GRUPO ID  TELEGRAM"

def send_telegram_message(message):
    """Envia uma mensagem para o Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Mensagem enviada com sucesso ao Telegram!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code} - {response.text}")

def process_alerts(alert_file_path):
    """Processa os alertas do arquivo JSON e envia mensagens para o Telegram"""
    try:
        # Processa o arquivo linha por linha
        with open(alert_file_path, 'r') as alert_file:
            for line in alert_file:
                try:
                    alert_json = json.loads(line.strip())
                    
                    # Extrai os campos necessários do JSON
                    rule = alert_json.get('rule', {})
                    agent = alert_json.get('agent', {})
                    data = alert_json.get('data', {})

                    # Formata a mensagem com os campos necessários
                    message = (
                        f"⚠️ *Alerta Wazuh* ⚠️\n"
                        f"❌ *Descrição:* {rule.get('description', 'N/A')}\n"
                        f"⏰ *Timestamp:* {alert_json.get('timestamp', 'N/A')}\n"
                        f"☢️ *Nível:* {rule.get('level', 'N/A')}\n"
                        f"💡 *Agente:* {agent.get('name', 'N/A')} (ID: {agent.get('id', 'N/A')})\n"                        
                        f"📱 *IP:* {agent.get('ip', 'N/A')} (Porta: {data.get('srcport', 'N/A')})\n"  
                        f"📰 *Mitre:* {rule.get('mitre', 'N/A')}\n"                     
                        f"📑 *Log Completo:* {alert_json.get('full_log', 'N/A')}\n"
                    )

                    # Envia a mensagem para o Telegram
                    send_telegram_message(message)
                except json.JSONDecodeError as e:
                    print(f"Erro ao decodificar JSON na linha: {line.strip()} - Erro: {e}")
    except FileNotFoundError:
        print(f"Arquivo {alert_file_path} não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    # Chama o processamento com o caminho do arquivo JSON
    process_alerts(sys.argv[1])
