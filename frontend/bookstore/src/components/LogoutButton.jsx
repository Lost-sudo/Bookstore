import React, { useState } from "react";
import { useAuth } from "../context/AuthContext";
import { useNavigate } from "react-router-dom";

export default function LogoutButton() {
  const { logout } = useAuth();
  const navigate = useNavigate();
  const { loading, setLoading } = useState(false);

  const handleLogout = () => {
    logout();
    setLoading(true);
    setTimeout(() => {
      navigate("/login");
    }, 1000);
  };

  return (
    <button
      onClick={handleLogout} disabled={loading}
      className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-gray-800 hover:bg-white mt-4 lg:mt-0 disabled:opacity-50 disabled:cursor-not-allowed"
    >
      Logout
    </button>
  );
}
