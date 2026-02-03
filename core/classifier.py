def classify_contract(text):
    t = text.lower()
    if "employment" in t:
        return "Employment Agreement"
    if "vendor" in t or "supplier" in t:
        return "Vendor Agreement"
    if "lease" in t:
        return "Lease Agreement"
    if "partnership" in t:
        return "Partnership Deed"
    return "Service Agreement"
