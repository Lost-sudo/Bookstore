import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import LogoutButton from "./LogoutButton";

export default function Navbar() {
  const { isAuthenticated } = useAuth();

  return (
    <nav className="bg-gray-800 p-4 shadow-md">
      <div className="container mx-auto flex flex-wrap items-center justify-between">
        <div className="flex flex-items flex-shrink-0 text-white mr-6">
          <span className="font-semibold text-xl tracking-tight">
            Bookstore
          </span>
        </div>
        <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
          <div className="text-sm lg:flex-grow">
            <Link
              to="/"
              className="block mt-4 lg:inline-block lg:mt-0 text-gray-300 hover:text-white mr-4"
            >
              Home
            </Link>
            {isAuthenticated && (
              <Link
                to="/dashboard"
                className="block mt-4 lg:inline-block lg:mt-0 text-gray-300 hover:text-white mr-4"
              >
                Dashboard
              </Link>
            )}
          </div>
        </div>

        {isAuthenticated ? (
          <LogoutButton />
        ) : (
          <div className="flex space-x-4">
            <Link
              to="/login"
              className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-gray-800 hover:bg-white mt-4 lg:mt-0"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-gray-800 hover:bg-white mt-4 lg:mt-0"
            >
              Register
            </Link>
          </div>
        )}
      </div>
    </nav>
  );
}
