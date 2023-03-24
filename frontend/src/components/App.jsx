import React from "react";
import ReactDOM from "react-dom"
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./HomePage";
import WhereShouldIGo from "./WhereShouldIGoPage";
import CheckIn from "./CheckIn";
import LoginForm from "./LoginForm";
import CreateAccountForm from "./CreateAccountForm";


function App() {
  return (
    <div>

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />}/>
        <Route path="/homepage" element={<HomePage />}/>
          <Route path="/whereshouldigo" element={<WhereShouldIGo />} />
          <Route path="/checkin" element={<CheckIn />} />
          {/* <Route path="*" element={error page} /> */}
  
      </Routes></BrowserRouter>

    </div>
  );
}

export default App;
