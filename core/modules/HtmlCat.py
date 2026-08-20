def htmlcat_run(result):
       print("="*59)
       print("\n\t\t\tHTMLCAT")
       print("="*59)
       print("\n")

       url = result["url"]
       html = result["response"].text
       print(f"Html Page:\n{html}")
       print("-"*59)


