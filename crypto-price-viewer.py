#include <Trade\Trade.mqh>   // Trading library

CTrade trade;                // Create trade object

// User settings
input double LotSize      = 0.10;    // Lot size
input double TP_Percent   = 0.10;    // Take profit in %
input double SL_Percent   = 0.05;    // Stop loss in %
input double MaxSpread    = 3.0;     // Max spread allowed (in points)

bool tradePlaced = false;   // To ensure only first tick trade

void OnTick()
{
   // If trade already placed, do nothing
   if(tradePlaced) return;
   
   // Check if no position open for this symbol
   if(!PositionSelect(_Symbol))
   {
      // Spread check
      double spread = (Ask - Bid) / _Point;
      if(spread > MaxSpread)
      {
         Print("Spread too high: ", spread, " points. No trade opened.");
         return;
      }

      // Price levels
      double price = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
      double tp    = price + (price * TP_Percent / 100.0);
      double sl    = price - (price * SL_Percent / 100.0);

      // Normalize prices
      tp = NormalizeDouble(tp, _Digits);
      sl = NormalizeDouble(sl, _Digits);

      // Send buy order
      if(trade.Buy(LotSize, _Symbol, price, sl, tp))
      {
         Print("Buy order placed successfully! TP: ", tp, " | SL: ", sl);
         tradePlaced = true;  // Only first tick
      }
      else
      {
         Print("Order failed: ", _LastError);
      }
   }
}
