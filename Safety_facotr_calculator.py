def safety_factor(ultimate_strength, allowable_stress):
    safety_record = allowable_stress / ultimate_strength if ultimate_strength != 0 else 0
    return safety_record

def safety_factor_check():
    while True:
        ultimate_strength = float(input("극한강도를 입력하세요: "))
        allowable_stress = float(input("허용응력을 입력하세요: "))

        safety = safety_factor(ultimate_strength, allowable_stress)

        print("안전계수:", safety)

        if safety >= 1:
            print("안전계수가 1 이상입니다. 안전합니다.")

        else:
            print("안전계수가 1 미만입니다. 위험합니다.")

        choice = input("더 계산하시겠습니까? (Y/N): ")
        if choice.upper() != 'Y':
            break

if __name__ == "__main__":
    safety_factor_check()

