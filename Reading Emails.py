import imaplib
import email
from email.header import decode_header
from getpass import getpass


def decode_subject(subject):
    if not subject:
        return "(No Subject)"

    decoded_parts = decode_header(subject)
    final_subject = ""

    for part, encoding in decoded_parts:
        if isinstance(part, bytes):
            final_subject += part.decode(encoding or "utf-8", errors="ignore")
        else:
            final_subject += part

    return final_subject


def get_unread_subjects(gmail_user, app_password, limit=10):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(gmail_user, app_password)

        # readonly=True ensures emails are not marked as read
        mail.select("INBOX", readonly=True)

        status, data = mail.uid("search", None, "UNSEEN")

        if status != "OK":
            print("Could not search unread emails.")
            return

        email_uids = data[0].split()

        if not email_uids:
            print("No unread emails found.")
            return

        latest_uids = email_uids[-limit:][::-1]

        print(f"\nLatest {len(latest_uids)} unread email subjects:\n")

        for index, uid in enumerate(latest_uids, start=1):
            status, msg_data = mail.uid(
                "fetch",
                uid,
                "(BODY.PEEK[HEADER.FIELDS (SUBJECT)])"
            )

            if status != "OK":
                continue

            raw_header = msg_data[0][1]
            msg = email.message_from_bytes(raw_header)

            subject = decode_subject(msg.get("Subject"))
            print(f"{index}. {subject}")

        mail.logout()

    except imaplib.IMAP4.error:
        print("Login failed. Check your Gmail address, App Password, and IMAP settings.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    gmail_user = input("Enter your Gmail address: ")
    app_password = input("Enter your Gmail App Password: ").replace(" ", "")

    get_unread_subjects(gmail_user, app_password)
