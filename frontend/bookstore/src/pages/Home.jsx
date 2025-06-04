export default function Home() {
  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white shadow-md rounded-lg p-6">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">
          Welcome to Bookstore
        </h1>
        <p className="text-gray-600 mb-6">
          Discover the world of knowledge with our extensive collection of books. From bestsellers to rare finds, we have something for every reader.
        </p>
        <div className="bg-gray-50 p-4 rounded-md border border-gray-200">
          <h2 className="text-xl font-semibold text-gray-700 mb-2">Feature Books</h2>
          <p className="text-gray-600">
            Check back soon to see our featured books and special offers.
          </p>
        </div>
      </div>
    </div>
  );
}