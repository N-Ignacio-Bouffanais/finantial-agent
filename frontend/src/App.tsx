import { useDispatch, useSelector } from "react-redux";
import { RootState, AppDispatch } from "./store/store";
import { useState } from "react";
import { sendMessage, addMessage } from "./store/chatSlice";

const App = () => {
  const dispatch = useDispatch<AppDispatch>();
  const messages = useSelector((state:RootState) => state.chat.messages);
  const loading = useSelector((state:RootState) => state.chat.loading);
  const [input, setInput] = useState("");

  const handleSendMessage = () => {
    if (input.trim()) {
      dispatch(addMessage({ sender: "user", text: input }));
      dispatch(sendMessage(input));
      console.log(input)
      setInput("");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-300 p-4">
      <h1 className="text-3xl font-bold underline p-2">
        Chat con RAG y LangChain
      </h1>

      <div className="flex flex-col w-full max-w-lg bg-white shadow-md rounded-lg p-4 mt-4">
        <div className="flex-grow overflow-auto h-60 border rounded p-2">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-2 ${
                msg.sender === "user" ? "text-blue-600" : "text-gray-600"
              }`}
            >
              <strong>{msg.sender}:</strong> {msg.text}
            </div>
          ))}
        </div>

        <div className="flex gap-2 mt-4">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Escribe tu mensaje..."
            className="flex-grow border rounded p-2"
          />
          <button
            onClick={handleSendMessage}
            disabled={loading}
            className="bg-blue-500 text-white px-4 py-2 rounded"
          >
            {loading ? "Enviando..." : "Enviar"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;
