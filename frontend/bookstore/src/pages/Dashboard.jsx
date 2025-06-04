import { useAuth } from "../context/AuthContext";

export default function Dashboard() {
  const { user } = useAuth();
  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white shadow-md rounded-lg p-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Dashboard</h1>
        <div className="bg-blue-50 border-l-4 border-blue-500 p-4 mb-6">
          <p className="text-blue-700">
            Welcome,{" "}
            {user?.username || user?.email || user?.full_name || "User"}! You're
            now logged in to your account.
          </p>
        </div>
        <div className="grid grid-cold-1 md:grid-cols-2 gap-6">
          <div className="bg-gray-50 p-4 rounded-md border border-gray-200">
            <h2 className="text-xl font-semibold text-gray-700 mb-2">
              My Books
            </h2>
            <p className="text-gray-600">
              You haven't added any books to your collection yet.
            </p>
          </div>
          <div className="bg-gray-50 p-4 rounded-md border border-gray-200">
            <h2 className="text-xl font-semibold text-gray-700 mb-2">
              Reading List
            </h2>
            <p className="Your reading list is empty. Start adding books to track your reading progress."></p>
          </div>
        </div>
      </div>
    </div>
  );
}
