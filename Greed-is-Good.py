def score(dice):
    point = 0
    numberCollections = {}

    # Mencari Jumlah nomor yang sama ada berapa,disimpan dalam bentuk dictionary
    for num in dice:
        if numberCollections.get(num,0) >= 1:
            numberCollections[num] = numberCollections.get(num) + 1
        else :
            numberCollections[num] = numberCollections.get(num,0) + 1
            
    # mencari nomor yang jumlahnya lebih dari atau sama dengan 3 
    for key in numberCollections :
        if numberCollections[key] >= 3 :
            if key == 1 :
                point += 1000
                numberCollections[key] = numberCollections.get(key) - 3
            else :
                point += key * 100
                numberCollections[key] = numberCollections.get(key) - 3
                
    # mengecek kembali apakah masih tersisa bilangan 1 dan 5
    for key in numberCollections :
        if key == 1 :
            point += 100 * numberCollections[key]
        elif key == 5 :
            point += 50 * numberCollections[key]
        else :
            pass

    
    return point
