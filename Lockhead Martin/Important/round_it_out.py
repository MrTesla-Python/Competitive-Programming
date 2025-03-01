from decimal import (
    Decimal,
    ROUND_HALF_UP, ROUND_HALF_DOWN,
    ROUND_UP, ROUND_DOWN,
    ROUND_HALF_EVEN, ROUND_05UP
)

for _ in range(int(input().strip())):
    num_str, method, places_str = input().split()
    num = Decimal(num_str)
    places = int(places_str)
    
    # Build quantization exponent as a Decimal.
    # For places >= 0, e.g. 1 => "1e-1" => Decimal("0.1")
    # For places < 0, e.g. -1 => "1e1" => Decimal("10")
    if places >= 0:
        quant_str = "1e-" + str(places)
    else:
        quant_str = "1e" + str(abs(places))
    quant = Decimal(quant_str)
    
    # Apply the specified rounding mode.
    if method == "HU":
        num = num.quantize(quant, rounding=ROUND_HALF_UP)
    elif method == "HD":
        num = num.quantize(quant, rounding=ROUND_HALF_DOWN)
    elif method == "U":
        num = num.quantize(quant, rounding=ROUND_UP)
    elif method == "D":
        num = num.quantize(quant, rounding=ROUND_DOWN)
    elif method == "HE":
        num = num.quantize(quant, rounding=ROUND_HALF_EVEN)
    elif method == "HO":
        num = num.quantize(quant, rounding=ROUND_05UP)
    
    # If rounding to a negative place, we output an integer (no decimal part).
    if places < 0:
        print(int(num))
    else:
        # Convert to fixed-point string (e.g. "1.20"), then strip trailing zeros.
        s = format(num, "f")               # e.g. "1.20"
        if "." in s:
            s = s.rstrip("0").rstrip(".")  # e.g. "1.2"
        if s == "":
            s = "0"                        # Handle the edge case of "0.0" -> ""
        print(s)
