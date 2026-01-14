from telethon import TelegramClient
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
import pandas as pd
from config import API_ID, API_HASH, GROUP_LINK, SESSION_NAME


def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    client.start()

    print('🚀 Starting members export...')

    members = []

    for user in client.iter_participants(GROUP_LINK):
        is_admin = isinstance(
            user.participant,
            (ChannelParticipantAdmin, ChannelParticipantCreator)
        )

        members.append({
            'user_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_bot': user.bot,
            'is_admin': is_admin,
            'is_deleted': user.deleted
        })

    client.disconnect()

    df = pd.DataFrame(members)

    df.to_csv('members.csv', index=False, encoding='utf-8-sig')
    df.to_excel('members.xlsx', index=False)

    print(f'✅ Done! Exported {len(df)} members.')


if __name__ == '__main__':
    main()
