if __name__ == "__main__":
   try:
       __import__("ins").keycheck()
   except Exception as e:
       exit(str(e))
