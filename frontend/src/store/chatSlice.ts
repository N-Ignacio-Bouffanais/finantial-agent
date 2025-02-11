import { createSlice, PayloadAction, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

// Definir el tipo del estado del chat
interface ChatState {
  messages: { sender: "user" | "assistant"; text: string }[];
  loading: boolean;
  error: string | null;
}

// Estado inicial del chat
const initialState: ChatState = {
  messages: [],
  loading: false,
  error: null,
};

// Acción asincrónica para enviar mensajes al backend de FastAPI
export const sendMessage = createAsyncThunk(
  "chat/sendMessage",
  async (message: string, { rejectWithValue }) => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/chat/",
        { question: message },
        { headers: { "Content-Type": "application/json" } }
      );
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        return rejectWithValue(error.response?.data || "Error en la petición");
      }
      return rejectWithValue("Ocurrió un error desconocido");
    }
  }
);

// Definir el slice de Redux
const chatSlice = createSlice({
  name: "chat",
  initialState,
  reducers: {
    addMessage: (
      state,
      action: PayloadAction<{ sender: "user" | "assistant"; text: string }>
    ) => {
      state.messages.push(action.payload);
    },
    clearChat: (state) => {
      state.messages = [];
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(sendMessage.pending, (state) => {
        state.loading = true;
      })
      .addCase(sendMessage.fulfilled, (state, action) => {
        state.loading = false;
        state.messages.push({
          sender: "assistant",
          text: action.payload.response,
        });
      })
      .addCase(sendMessage.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

// Exportar acciones y reducer
export const { addMessage, clearChat } = chatSlice.actions;
export default chatSlice.reducer;
