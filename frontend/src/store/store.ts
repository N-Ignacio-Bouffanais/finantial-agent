import { configureStore } from "@reduxjs/toolkit";
import chatReducer from "./chatSlice";

export const store = configureStore({
  reducer: {
    chat: chatReducer,
  },
});

// Definir los tipos de RootState y AppDispatch
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
