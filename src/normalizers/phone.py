import phonenumbers


def normalize_phone(phone):

    if not phone:
        return None

    try:
        parsed = phonenumbers.parse(
            str(phone),
            "IN"
        )

        if phonenumbers.is_valid_number(parsed):
            return phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164
            )

    except Exception:
        pass

    return None
