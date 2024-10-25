from config import BOT_VERSION

WELCOME_TEXT = (
        "<b>🎉 SoloNet — твой доступ в свободный интернет! 🌐✨</b>\n\n"
        "<b>Наши преимущества:</b>\n"
        "<blockquote>"
        "🚀 <b>Высокая скорость</b>\n"
        "🔄 <b>Стабильность</b>\n"
        "🌍 <b>Смена локаций</b>\n"
        "💬 <b>Отзывчивая поддержка</b>\n"
        "📱💻 <b>Для телефонов, компьютеров и планшетов</b>\n"
        "💰 <b>Реферальная программа: 25% от покупки</b>\n"
        "</blockquote>"
        "\n\n🎁 <b>1 день бесплатно!</b>\n\n" 
        "<i>Перейдите в профиль для продолжения 👇</i>"
    )

ABOUT_VPN = (
        "*О VPN*\n\n"
        "<b>🚀 Высокоскоростные серверы</b>\n"
        "Мы используем высокоскоростные серверы в различных локациях для обеспечения стабильного и быстрого соединения.\n\n"
        
        "<b>🔐 Безопасность данных</b>\n"
        "Для защиты ваших данных мы применяем новейшие протоколы шифрования, которые гарантируют вашу конфиденциальность.\n\n"
        
        "<b>🔑 Ваш ключ — ваша безопасность!</b>\n"
        "Не передавайте своё шифрование сторонним лицам, чтобы избежать рисков.\n\n"
        
        f"<i>Версия бота: {BOT_VERSION}</i>" 
    )

KEY = (
        "<b>⚠️ У вас уже был пробный ключ.</b>\n\n"
        "Новый ключ будет выдан на <b>один месяц</b> и стоит <b>100 рублей</b>.\n\n"
        "<i>Хотите продолжить?</i>"
)

KEY_TRIAL = (
        "<b>🎉 Вам будет выдан пробный ключ на 24 часа!</b>\n\n"
        "<i>Пожалуйста, введите название для вашего пробного ключа:</i>"
)

TRIAL = (
        "🎉 Вам предоставлен пробный период на 1 день!\n"
        "Пожалуйста, воспользуйтесь им, чтобы протестировать наш сервис."
        )

NULL_BALANCE = (
        "❗️ Недостаточно средств на балансе для создания нового ключа. "
        "Пожалуйста, пополните баланс."
)

NO_KEYS = (
        "<b>У вас нет подключённых устройств</b> 😕\n\n"
        "➕ <b>Создайте первое устройство, чтобы подключиться к VPN</b>.\n"
        "Ваши устройства будут отображаться здесь."
)

INSTRUCTIONS = (
            "*📋 Инструкции по использованию вашего ключа:*\n\n"
        "1. **Скачайте приложение для вашего устройства:**\n"
        "   - **Для Android:** [V2Ray](https://play.google.com/store/apps/details?id=com.v2ray.ang&hl=ru&pli=1)\n"
        "   - **Для iPhone:** [Streisand](https://apps.apple.com/ru/app/streisand/id6450534064)\n"
        "   - **Для Windows:** [Hiddify Next](https://github.com/hiddify/hiddify-next/releases/latest/download/Hiddify-Windows-Setup-x64.Msix)\n\n"
        "2. **Скопируйте предоставленный ключ**, который вы получили ранее.\n"
        "3. **Откройте приложение и нажмите на плюсик сверху справа.**\n"
        "4. **Выберите 'Вставить из буфера обмена' для добавления ключа.**\n\n"
        "💬 Если у вас возникнут вопросы, не стесняйтесь обращаться в [поддержку](https://t.me/solonet_sup)."
)

def key_message_success(connection_link, remaining_time_message):
    key_message = (
        "✅ Ключ успешно создан:\n"
        f"<pre>{connection_link}</pre>\n\n"
        f"{remaining_time_message}\n\n"
        "<i>Добавьте ключ в приложение по инструкции ниже:</i>"
        )
    return key_message

def key_message(key, formatted_expiry_date, days_left_message, server_name):
    response_message = (f"🔑 <b>Ваш ключ:</b>\n<pre>{key}</pre>\n"
        f"📅 <b>Дата окончания:</b> {formatted_expiry_date}\n"
        f"{days_left_message}\n"
        f"🌍 <b>Сервер:</b> {server_name}\n\n" 
        f"<i>Скопируйте ключ и перейдите в инструкции👇</i>") 
    return response_message

def key_relocated(new_key):
    response_message = (
        f"Ключ успешно перемещен на новый сервер.\n\n"
        f"<b>Удалите старый ключ из вашего приложения и используйте новый для подключения к новому серверу:</b>\n"
        f"<pre>{new_key}</pre>"
                        )
    return response_message

def profile_message_send(username, tg_id, balance, key_count):
    profile_message = (
        f"<b>Профиль: {username}</b>\n\n"
        f"🔹 <b>ID:</b> {tg_id}\n"
        f"🔹 <b>Баланс:</b> {balance} RUB\n"
        f"🔹 <b>К-во устройств:</b> {key_count}\n\n"
        )
    return profile_message

def invite_message_send(referral_link,referral_stats):
    invite_message = (
        f"👥 <b>Ваша реферальная ссылка:</b>\n<pre>{referral_link}</pre>\n"
        f"<i>Пригласите реферала и получайте 25% с его каждого пополнения!</i>\n\n"
        f"🔹 <b>Всего приглашено:</b> {referral_stats['total_referrals']}\n"
        f"🔹 <b>Активных рефералов:</b> {referral_stats['active_referrals']}"
    )
    return invite_message