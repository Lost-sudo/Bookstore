import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { signupApi } from "../api/auth";

export default function Register() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();
  const [apiError, setApiError] = useState("");
  const [apiSuccess, setApiSuccess] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    setApiError("");
    setApiSuccess("");
    if (data.password != data.confirm_password) {
      setApiError("Passwords do not match");
      return;
    }
    setLoading(true);

    const payload = {
      email: data.email,
      full_name: data.full_name,
      password: data.password,
      password2: data.confirm_password,
      phone_number: data.phone_number,
    };
    

    try {
      const response = await signupApi(payload);
      
      if (response.access && response.refresh) {
        localStorage.setItem("access", response.access);
        localStorage.setItem("refresh", response.refresh);
        setApiSuccess("Registration successful! Redirecting....");
        setTimeout(() => {
          navigate("/dashboard");
        }, 2000);
      } else {
        setApiError(response.detail || "Registration failed");
      }
    } catch (error) {
      setApiError(error.message || "Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto">
      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6 text-center">
          Sign Up
        </h2>
        <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
          <div>
            <label
              htmlFor="full_name"
              className="block text-sm font-medium text-gray-700 mb-1"
            >
              Full Name
            </label>
            <input
              type="text"
              id="full_name"
              {...register("full_name", { required: "Full name is required" })}
              placeholder="Full Name"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            {errors.full_name && (
              <span className="text-red-500 text-sm">
                This field is required
              </span>
            )}
          </div>
          <div>
            <label
              htmlFor="email"
              className="block text-sm font-medium text-gray-700"
            >
              Email
            </label>
            <input
              type="email"
              id="email"
              {...register("email", {
                required: "Email is required",
                pattern: {
                  value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                  message: "Invalid email address",
                },
              })}
              placeholder="Email"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            {errors.email && (
              <span className="text-red-500 text-sm">
                This field is required
              </span>
            )}
          </div>
          <div>
            <label
              htmlFor="phone_number"
              className="block text-sm font-medium text-gray-700"
            >
              Phone Number
            </label>
            <input
              type="tel"
              id="phone_number"
              {...register("phone_number", {required: "Phone number is required"})}
              placeholder="Phone Number"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            {errors.phone_number && (
              <span className="text-red-500 text-sm">
                This field is required
              </span>
            )}
          </div>
          <div>
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-700"
            >
              Password
            </label>
            <input
              type="password"
              id="password"
              {...register("password", {
                required: "Password is required",
                minLength: {
                  value: 8,
                  message: "Password must be at least 8 characters",
                },
              })}
              placeholder="Password"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            {errors.password && (
              <span className="text-red-500 text-sm">
                This field is required
              </span>
            )}
          </div>
          <div>
            <label
              htmlFor="confirm_password"
              className="block text-sm font-medium text-gray-700"
            >
              Confirm Password
            </label>
            <input
              type="password"
              id="confirm_password"
              {...register("confirm_password", {
                required: "Please confirm your password",
                validate: (value) =>
                  value === watch("password") || "Passwords do not match",
              })}
              placeholder="Confirm Password"
              className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
            {errors.confirm_password && (
              <span className="text-red-500 text-sm">
                This field is required
              </span>
            )}
          </div>
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {loading ? "Loading..." : "Register"}
          </button>
        </form>
      </div>

      {apiError && (
        <div className="mt-4 p-3 bg-red-50 border border-red-200">
          <span className="text-red-500 text-sm">{apiError}</span>
        </div>
      )}
      {apiSuccess && (
        <div className="mt-4 p-3 bg-green-50 border border-green-200">
          <span className="text-green-500 text-sm">{apiSuccess}</span>
        </div>
      )}
    </div>
  );
}
