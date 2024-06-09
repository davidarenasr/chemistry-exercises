# The compound vanillin (used for flavoring ice cream and other foods) 
# is a substance whose aroma is detected by humans in very small quantities. The threshold limit is 2.0 x 10^-11 g per liter of air. If the current price for 50 grams of vanillin is $112, determine the cost for the aroma 
# of vanillin to be detectable in an aircraft hangar with a volume of 5.0 x 10^7 cubic feet

volume_pies = 5.0e7
volume_liter = volume_pies * 28.3168
umbral_limit =  2.0e-11
threshold_limit_grams = volume_liter * umbral_limit
price_gr = 112

hangar_prices = (price_gr/50) * volume_liter * umbral_limit

print ("the prices for threshold_limit_grams es equal a " + str(hangar_prices)) 
 