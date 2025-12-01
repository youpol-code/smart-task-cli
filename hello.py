from typing import List
def main():
    tasks :List[str] = []

    print("--- Smart Task CLI v1.0 ---")

    while True:
        new_task :str = input("ป้อนงานที่ต้องทำ (หรือพิมพ์ 'exit' เพื่อจบ):")

        if new_task == "exit":
            print("บ๊ายบาย! จบการทำงาน")
            break
        
        tasks.append(new_task)

        print(f"บันทึก: {new_task}")
        print(f"รายการทั้งหมด: {tasks}")
        print("-"*30)

if __name__ == "__main__":
    main()